import unittest
import os
from chatserver import ChatServer

class TestChat(unittest.TestCase):

    def setUp(self):
        self.chat = ChatServer()
        
    def tearDown(self):
        #self.chat.dispose()
        self.chat = None

    def test_WhenAliceHasPostedNoMessagesUserReadsEmptyTimeline(self):
        expected = ''
        actual = self.chat.action("Alice")
        self.assertEqual(actual, expected)        

    def test_WhenAliceHasPostedOneMessageUserCanReadOneTimelineMessage(self):
        expected = r"^Alice - I love the weather today"
        chatline = self.chat.action("Alice -> I love the weather today")
        actual = self.chat.action("Alice")
        self.assertRegexpMatches(actual, expected)

    @unittest.skip("not implemented")
    def test_WhenUserReadsAliceTimelineMessageItDisplaysTimeSincePosted(self):
        expectedtimeformat = r"\s\(.+\)$"
        expectedtime = r"\d+\s[minute|second]+[s]*\sago"  # r"\s\(\d+\s[minute|second]+[s]*\sago\)$"

        chatline = self.chat.action("Alice -> I love the weather today")
        actual = self.chat.action("Alice")        
        self.assertRegexpMatches(actual, expectedtimeformat)
        self.assertRegexpMatches(actual, expectedtime)

    @unittest.skip("not implemented")
    def test_WhenBobHasPostedTwoMessagesUserReadsBobsTwoTimelineMessages(self):
        pass

    @unittest.skip("not implemented")
    def test_WhenCharlieFollowsAliceThenCharlieReadsCharlieAndAliceMessagesOnCharlieWall(self):
        pass
    
    @unittest.skip("not implemented")
    def test_WhenCharlieFollowsBobAndAliceThenCharlieReadsCharlieBobAndAliceMessagesOnCharliesWall(self):
        pass

    @unittest.skip("not implemented")
    def test_WhenCharlieReadsCharliesWallBobsMessagesDisplaysTimeSincePosted(self):
        pass
    

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print "Tests Complete" #To stop the exit error in unittest library
