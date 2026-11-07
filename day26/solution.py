def should_deploy(stages):
    # TODO: True only if the stage list is non-empty and every
    # stage dict has status == "pass".
    pass

def bump_version(current, level):
    # TODO: bump a MAJOR.MINOR.PATCH string by level
    # ("major"/"minor"/"patch"), resetting lower parts to 0.
    pass

def pipeline_result(stages, current, level):
    # TODO: deploy the bumped version if should_deploy, else "BLOCKED".
    pass
