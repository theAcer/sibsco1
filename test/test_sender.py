#!/usr/bin/env python
# -*- coding: utf-8 *-*
import unittest
import sender
# emulator api key, no real sending

TEST_PHONE = "254717768380"
SAMPLETEXT = "Some text body"


class SmsTests(unittest.TestCase):

    def testSingleSendNexmo(self):
        client = sender.NexmoProvider(TEST_PHONE,SAMPLETEXT)
        client.defaultSender = "INFORM"

        result = client.send_sms(TEST_PHONE, SAMPLETEXT)

        self.assertEqual(result['send'][0]['text'], 'Some text body')
        self.assertEqual(result['send'][0]['to'], TEST_PHONE)

    def testSingleSendAfrica(self):
        client = sender.AfricastalkingProvider(TEST_PHONE,SAMPLETEXT)
        client.defaultSender = "6434"

        result = client.send_sms(TEST_PHONE, SAMPLETEXT)

        self.assertEqual(result['send'][0]['text'], 'Some text body')
        self.assertEqual(result['send'][0]['to'], TEST_PHONE)




def main():
    unittest.main()

if __name__ == '__main__':
    main()
