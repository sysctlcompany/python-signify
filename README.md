# python-signify - OpenBSD Signify for Python

0.0.0-DEVEL

Signify was originally written for OpenBSD to sign files and packages. This projects contains some code for working with signify keys/signatures from Python.

Specifically this project contains two modules: one that uses the `subprocess` module and one that simply re-implements Signify functionality directly.

## Module 1: Subprocess based wrapper around signify(1)

This is a fairly simple (subprocess based) wrapper around the OpenBSD signify(1) command. It basically does two things for you to make your life a little bit easier:

- It handles thread safety and the actual calling of subprocess, which is easy to screw up.
- For convenience it will aid you in juggling temporary files in case you want to work with strings/buffers instead of paths, as signify(1) work on paths.

Please make sure you read and understand the library docstrings before you use the code. There are some security considerations.

### Example

```python
from signify import Signify

pubkey = """untrusted comment: bjorntest public key
RWQ100QRGZoxU+Oy1g7Ko+8LjK1AQLIEavp/NuL54An1DC0U2cfCLKEl
"""

signature = """untrusted comment: signature from bjorntest secret key
RWQ100QRGZoxU/gjzE8m6GYtfICqE0Ap8SdXRSHrpjnSBKMc2RMalgi5RKrEHmKfTmcsuB9ZzDCo6K6sYEqaEcEnnAFa0zCewAg=
"""

message = """my message
"""

print Signify().verify_simple(pubkey, signature, message)
broken_sig = signature.replace('Malgi', 'Magic')
print Signify().verify_simple(pubkey, broken_sig, message)
```

## Module 2: "Pure" Python version

The `signify.pure` module has a Python implementation of some parts of `signify`, without requiring the signify binary or the subprocess module. This code requires the Python bcrypt and ed25519 modules.

### Dependencies

- [python-ed25519](https://github.com/warner/python-ed25519]) (`pip install ed25519`)
- [py-bcrypt](py-bcrypt) (`pip install py-bcrypt`)

### Example

The API is sort of similar to the one above.

## About

Copyright Björn Edström 2015. See LICENSE for details.
