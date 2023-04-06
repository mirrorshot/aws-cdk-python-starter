import os
import subprocess
import sys
from distutils.dir_util import copy_tree, remove_tree
from pathlib import Path

import pip
import pytest

test_result = pytest.main(["-sv", "tests"])
if test_result != 0:
    exit(test_result)

remove_tree(directory=".build/python")

libs_requirements = "./libraries/requirements.txt"
if Path(libs_requirements).is_file():
    pip.main(["install", "-r", libs_requirements, "--target", ".build/python"])
lambdas_requirements = "./lambdas/requirements.txt"
if Path(lambdas_requirements).is_file():
    pip.main(["install", "-r", lambdas_requirements, "--target", ".build/python"])

copy_tree(
    src="libraries",
    dst=".build/python",
)

if len(sys.argv) >= 4:
    os.environ['CDK_DEPLOY_ACCOUNT'] = sys.argv[1]
    os.environ['CDK_DEPLOY_REGION'] = sys.argv[2]
    os.environ['CDK_DEPLOY_ENVIRONMENT'] = sys.argv[3]
    args = sys.argv[4:]
    subprocess.run(['npx', 'cdk', 'deploy', '--all'] + args, shell=True, check=True)
else:
    if os.path.exists('.env-locale'):
        with open('.env-locale') as f:
            for line in f:
                line = line.strip()
                if not line.startswith('#') and '=' in line:
                    name, value = line.split('=', 1)
                    os.environ[name] = value

        if os.environ.get('DEFAULT_ENV'):
            os.environ['CDK_DEPLOY_ACCOUNT'] = os.environ.get('DEFAULT_ACCOUNT')
            os.environ['CDK_DEPLOY_REGION'] = os.environ.get('DEFAULT_REGION')
            os.environ['CDK_DEPLOY_ENVIRONMENT'] = os.environ.get('DEFAULT_ENV')
            args = sys.argv[1:]
            subprocess.run(['npx', 'cdk', 'deploy', '--all'] + args, shell=True, check=True)
            sys.exit(0)

    print("Provide account, region, and environment as first three args.")
    print("Additional args are passed through to cdk deploy.")
    sys.exit(1)
