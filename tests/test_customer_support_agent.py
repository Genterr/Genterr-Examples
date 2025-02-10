import unittest
import asyncio
from agents.customer_support_agent import main

class TestCustomerSupportAgent(unittest.TestCase):
    def test_process_task(self):
        result = asyncio.run(main())
        self.assertIn("How can I help you today?", result['result'])

if __name__ == "__main__":
    unittest.main()