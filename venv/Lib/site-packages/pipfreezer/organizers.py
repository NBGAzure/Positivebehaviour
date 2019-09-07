from . import config
from .utils import get_list, item_to_label


def organize_packages(key, known_packages, package_list):
    """Organize known packages."""
    packages = []
    # comment = known_packages.pop(0).title()
    # print(comment)
    packages.append('\n# %s' % item_to_label(key))
    to_remove = []
    # known_packages.reverse()
    # print('package_list:', package_list)
    # print('known_packages:', known_packages)
    for p in package_list:
        if any(kp in p for kp in known_packages):
            packages.append(p)
            to_remove.append(p)

    # Remove packages from package_list
    # print('To remove:', to_remove)
    for p in to_remove:
        # print(p)
        if p in package_list:
            #  print('Remove:', p)
            package_list.remove(p)

    packages.sort()

    if len(packages) > 1:
        # print(packages)
        return packages
    return []


def organize(section, target_list):
    """Get the items in a section and organize them."""
    items = list(config.items(section))
    for key, val in items:
        if 'packages' not in key:
            packages = get_list(config, section, key)
            org_packages = organize_packages(key, packages, target_list)
            target_list += org_packages
            # print(key)

    return target_list
