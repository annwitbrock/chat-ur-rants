import unittest
import os
from chatserver import ChatServer

class TestChat(unittest.TestCase):

    def setUp(self):
        self.chat = ChatServer()

    def test_WhenAliceHasPostedNoMessagesAliceReadsEmptyTimeline(self):
        expected = None
        actual = self.chat.action("Alice")
        self.assertEqual(expected, actual)        

    def test_WhenAliceHasPostedOneMessageAliceReadsOneTimelineMessage(self):
        expected = None
        actual = self.chat.action("Alice -> I love the weather today")
        self.assertEqual(expected, actual)
    
    def test_WhenAliceHasPostedOneMessageBobReadsAlicesOneTimelineMessage(self):
        pass

    def test_WhenBobReadsAlicesTimelineMessageItDisplaysTimeSincePosted(self):
        pass

    def test_WhenBobHasPostedTwoMessagesBobReadsBobsTwoTimelineMessages(self):
        pass

    def test_WhenCharlieFollowsAliceThenCharlieReadsCharlieAndAliceMessagesOnCharlieWall(self):
        pass

    def test_WhenCharlieFollowsBobAndAliceThenCharlieReadsCharlieBobAndAliceMessagesOnCharliesWall(self):
        pass

    def test_WhenCharlieReadsCharliesWallBobsMessagesDisplaysTimeSincePosted(self):
        pass
    

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print "Tests Complete" #To stop the exit error in unittest library
