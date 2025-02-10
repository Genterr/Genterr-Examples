import unittest
import asyncio
from agents.simple_agent import main

class TestSimpleAgent(unittest.TestCase):
    def test_process_task(self):
        result = asyncio.run(main())
        self.assertIn("Hello, Genterr!", result['result'])

if __name__ == "__main__":
    unittest.main()