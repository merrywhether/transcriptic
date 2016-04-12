"""
Big dumb file of routes, please do not add any logic into this file
Note: {api_root} and {org_id} are automatically supplied in the Connection.get_route and do not need to be specified
"""


def create_project(api_root, org_id):
    return "{api_root}/{org_id}".format(**locals())


def delete_project(api_root, org_id, project_id):
    return "{api_root}/{org_id}/{project_id}".format(**locals())


def archive_project(api_root, org_id, project_id):
    return "{api_root}/{org_id}/{project_id}".format(**locals())


def get_project(api_root, org_id, project_id):
    return "{api_root}/{org_id}/{project_id}".format(**locals())


def get_projects(api_root, org_id):
    return "{api_root}/{org_id}/?q=&per_page=500".format(**locals())


def get_project_runs(api_root, org_id, project_id):
    return "{api_root}/{org_id}/{project_id}".format(**locals())


def create_package(api_root, org_id):
    return "{api_root}/{org_id}/packages".format(**locals())


def delete_package(api_root, org_id, package_id):
    return "{api_root}/{org_id}/packages/{package_id}".format(**locals())


def get_package(api_root, org_id, package_id):
    return "{api_root}/{org_id}/packages/{package_id}".format(**locals())


def get_packages(api_root, org_id):
    return "{api_root}/{org_id}/packages/".format(**locals())


def post_release(api_root, org_id, release_id):
    return "{api_root}/{org_id}/packages/{package_id}/releases/".format(**locals())


def get_release_status(api_root, org_id, release_id, timestamp):
    return "{api_root}/{org_id}/packages/{package_id}/releases/{release_id}?_={timestamp}".format(**locals())


def query_resources(api_root, query):
    return "{api_root}/_commercial/kits?q={query}&per_page=1000".format(**locals())


def get_quick_launch(api_root, org_id, project_id, quick_launch_id):
    return "{api_root}/{org_id}/{project_id}/runs/quick_launch/{quick_launch_id}".format(**locals())


def create_quick_launch(api_root, org_id, project_id):
    return "{api_root}/{org_id}/{project_id}/runs/quick_launch".format(**locals())
