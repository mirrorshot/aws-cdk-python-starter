import base64
import subprocess
import sys
from distutils.dir_util import mkpath
from pathlib import Path

project = Path(".").absolute().name.replace(" ", "_")

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    mode = "new"

if mode in ["new", "cdk"]:
    print("creating a new CDK python project")
    subprocess.run(['npx', 'cdk', 'init', 'app', '--language=python'], shell=True, check=True)

if not (mode in ["new", "extend"]):
    print("not including custom extensions")
    exit(0)

print("including custom extensions")

print("making directories")
mkpath(".build")
mkpath("lambdas")
mkpath("libraries")
mkpath("scripts")

print("extending .gitignore")
git_ignore = open(".gitignore", "a")
git_ignore.writelines([".build/"])
git_ignore.close()

print("extending requirements.txt")
requirements = open("requirements.txt", "a")
requirements.writelines(["aws_lambda_powertools==2.11.0"])
requirements.close()

print("creating .env-locale")
env_out = open(".env-locale", "w")
env_out.writelines([
    "DEFAULT_ACCOUNT=548682486172",
    "DEFAULT_REGION=eu-west-1",
    "DEFAULT_ENV=dev",
])
env_out.close()

print("extracting cdk-deploy-to.py")
scr_out = open("scripts/cdk-deploy-to.py", "w")
scr_out.write(base64.urlsafe_b64decode("""aW1wb3J0IG9zCmltcG9ydCBzdWJwcm9jZXNzCmltcG9ydCBzeXMKZnJvbSBkaXN0dXRpbHMuZGlyX
3V0aWwgaW1wb3J0IGNvcHlfdHJlZSwgcmVtb3ZlX3RyZWUKZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCgppbXBvcnQgcGlwCmltcG9ydCBweXRlc3QKCnRl
c3RfcmVzdWx0ID0gcHl0ZXN0Lm1haW4oWyItc3YiLCAidGVzdHMiXSkKaWYgdGVzdF9yZXN1bHQgIT0gMDoKICAgIGV4aXQodGVzdF9yZXN1bHQpCgpyZW1
vdmVfdHJlZShkaXJlY3Rvcnk9Ii5idWlsZC9weXRob24iKQoKbGlic19yZXF1aXJlbWVudHMgPSAiLi9saWJyYXJpZXMvcmVxdWlyZW1lbnRzLnR4dCIKaW
YgUGF0aChsaWJzX3JlcXVpcmVtZW50cykuaXNfZmlsZSgpOgogICAgcGlwLm1haW4oWyJpbnN0YWxsIiwgIi1yIiwgbGlic19yZXF1aXJlbWVudHMsICItL
XRhcmdldCIsICIuYnVpbGQvcHl0aG9uIl0pCmxhbWJkYXNfcmVxdWlyZW1lbnRzID0gIi4vbGFtYmRhcy9yZXF1aXJlbWVudHMudHh0IgppZiBQYXRoKGxh
bWJkYXNfcmVxdWlyZW1lbnRzKS5pc19maWxlKCk6CiAgICBwaXAubWFpbihbImluc3RhbGwiLCAiLXIiLCBsYW1iZGFzX3JlcXVpcmVtZW50cywgIi0tdGF
yZ2V0IiwgIi5idWlsZC9weXRob24iXSkKCmNvcHlfdHJlZSgKICAgIHNyYz0ibGlicmFyaWVzIiwKICAgIGRzdD0iLmJ1aWxkL3B5dGhvbiIsCikKCmlmIG
xlbihzeXMuYXJndikgPj0gNDoKICAgIG9zLmVudmlyb25bJ0NES19ERVBMT1lfQUNDT1VOVCddID0gc3lzLmFyZ3ZbMV0KICAgIG9zLmVudmlyb25bJ0NES
19ERVBMT1lfUkVHSU9OJ10gPSBzeXMuYXJndlsyXQogICAgb3MuZW52aXJvblsnQ0RLX0RFUExPWV9FTlZJUk9OTUVOVCddID0gc3lzLmFyZ3ZbM10KICAg
IGFyZ3MgPSBzeXMuYXJndls0Ol0KICAgIHN1YnByb2Nlc3MucnVuKFsnbnB4JywgJ2NkaycsICdkZXBsb3knLCAnLS1hbGwnXSArIGFyZ3MsIHNoZWxsPVR
ydWUsIGNoZWNrPVRydWUpCmVsc2U6CiAgICBpZiBvcy5wYXRoLmV4aXN0cygnLmVudi1sb2NhbGUnKToKICAgICAgICB3aXRoIG9wZW4oJy5lbnYtbG9jYW
xlJykgYXMgZjoKICAgICAgICAgICAgZm9yIGxpbmUgaW4gZjoKICAgICAgICAgICAgICAgIGxpbmUgPSBsaW5lLnN0cmlwKCkKICAgICAgICAgICAgICAgI
GlmIG5vdCBsaW5lLnN0YXJ0c3dpdGgoJyMnKSBhbmQgJz0nIGluIGxpbmU6CiAgICAgICAgICAgICAgICAgICAgbmFtZSwgdmFsdWUgPSBsaW5lLnNwbGl0
KCc9JywgMSkKICAgICAgICAgICAgICAgICAgICBvcy5lbnZpcm9uW25hbWVdID0gdmFsdWUKCiAgICAgICAgaWYgb3MuZW52aXJvbi5nZXQoJ0RFRkFVTFR
fRU5WJyk6CiAgICAgICAgICAgIG9zLmVudmlyb25bJ0NES19ERVBMT1lfQUNDT1VOVCddID0gb3MuZW52aXJvbi5nZXQoJ0RFRkFVTFRfQUNDT1VOVCcpCi
AgICAgICAgICAgIG9zLmVudmlyb25bJ0NES19ERVBMT1lfUkVHSU9OJ10gPSBvcy5lbnZpcm9uLmdldCgnREVGQVVMVF9SRUdJT04nKQogICAgICAgICAgI
CBvcy5lbnZpcm9uWydDREtfREVQTE9ZX0VOVklST05NRU5UJ10gPSBvcy5lbnZpcm9uLmdldCgnREVGQVVMVF9FTlYnKQogICAgICAgICAgICBhcmdzID0g
c3lzLmFyZ3ZbMTpdCiAgICAgICAgICAgIHN1YnByb2Nlc3MucnVuKFsnbnB4JywgJ2NkaycsICdkZXBsb3knLCAnLS1hbGwnXSArIGFyZ3MsIHNoZWxsPVR
ydWUsIGNoZWNrPVRydWUpCiAgICAgICAgICAgIHN5cy5leGl0KDApCgogICAgcHJpbnQoIlByb3ZpZGUgYWNjb3VudCwgcmVnaW9uLCBhbmQgZW52aXJvbm
1lbnQgYXMgZmlyc3QgdGhyZWUgYXJncy4iKQogICAgcHJpbnQoIkFkZGl0aW9uYWwgYXJncyBhcmUgcGFzc2VkIHRocm91Z2ggdG8gY2RrIGRlcGxveS4iK
QogICAgc3lzLmV4aXQoMSkK""").decode('ascii'))
scr_out.close()

print("extending stack __init__.py")
stack_out = open(project.replace("-", "_") + "/__init__.py", "a")
stack_out.write(base64.urlsafe_b64decode("""aW1wb3J0IG9zCgpmcm9tIGF3c19jZGsgaW1wb3J0ICgKICAgIGF3c19sYW1iZGEsCikKZnJvbSB
jb25zdHJ1Y3RzIGltcG9ydCBDb25zdHJ1Y3QKCkRFUExPWV9FTlZJUk9OTUVOVCA9IG9zLmdldGVudigiQ0RLX0RFUExPWV9FTlZJUk9OTUVOVCIpClJFR0
lPTiA9IG9zLmdldGVudigiQ0RLX0RFUExPWV9SRUdJT04iKQpFTlYgPSAiJXMtJXMiICUgKERFUExPWV9FTlZJUk9OTUVOVCwgUkVHSU9OKQpQQVRURVJOI
D0gImV4YW1wbGUtJXMtJXMiCgoKZGVmIG1ha2VfcmVzb3VyY2VfbmFtZShyZXNvdXJjZTogc3RyKToKICAgIHJldHVybiBQQVRURVJOICUgKEVOViwgcmVz
b3VyY2UpCgoKZGVmIGxpYnJhcmllc19sYXllcihzY29wZTogQ29uc3RydWN0KToKICAgIHJldHVybiBhd3NfbGFtYmRhLkxheWVyVmVyc2lvbigKICAgICA
gICBzY29wZT1zY29wZSwKICAgICAgICBpZD1tYWtlX3Jlc291cmNlX25hbWUoImxpYnJhcmllcyIpLAogICAgICAgIGxheWVyX3ZlcnNpb25fbmFtZT1tYW
tlX3Jlc291cmNlX25hbWUoImxpYnJhcmllcyIpLAogICAgICAgIGNvZGU9YXdzX2xhbWJkYS5Bc3NldENvZGUoIi5idWlsZCIpLAogICAgICAgIGNvbXBhd
GlibGVfcnVudGltZXM9W2F3c19sYW1iZGEuUnVudGltZS5QWVRIT05fM185XSwKICAgICAgICBjb21wYXRpYmxlX2FyY2hpdGVjdHVyZXM9WwogICAgICAg
ICAgICBhd3NfbGFtYmRhLkFyY2hpdGVjdHVyZS5YODZfNjQsCiAgICAgICAgXSwKICAgICAgICBkZXNjcmlwdGlvbj0ibGlicmFyaWVzIiwKICAgICkK"""
                                         ).decode('ascii').replace("example", project))
stack_out.close()
