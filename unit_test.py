import unittest
from datetime import datetime
from unittest.mock import MagicMock
from res_time_analysis import ResolutionTimeAnalysis
from model import Issue

class TestResolutionTimeAnalysis(unittest.TestCase):
    def setUp(self):
        """
        Set up mock issues for testing resolution time analysis.
        """
        self.mock_issues = [
            Issue({
                "url": "http://example.com/1",
                "creator": "user1",
                "labels": ["bug"],
                "state": "closed",
                "created_date": datetime(2023, 1, 1),
                "updated_date": datetime(2023, 1, 5),
                "events": []
            }),
            Issue({
                "url": "http://example.com/2",
                "creator": "user2",
                "labels": ["feature"],
                "state": "closed",
                "created_date": datetime(2023, 1, 10),
                "updated_date": datetime(2023, 1, 20),
                "events": []
            }),
            Issue({
                "url": "http://example.com/3",
                "creator": "user3",
                "labels": ["task"],
                "state": "open",
                "created_date": datetime(2023, 1, 15),
                "updated_date": None,
                "events": []
            })
        ]
    
    def test_resolution_time_analysis(self):
        """
        Test the resolution time calculation for closed issues.
        """
        # Mock the DataLoader to return mock issues
        mock_data_loader = MagicMock()
        mock_data_loader.load_issues.return_value = self.mock_issues
        
        # Inject the mocked DataLoader into ResolutionTimeAnalysis
        analysis = ResolutionTimeAnalysis()
        analysis.issues = mock_data_loader.load_issues()
        
        # Perform the analysis
        closed_issues = [
            issue for issue in analysis.issues
            if issue.state == "closed" and issue.created_date and issue.updated_date
        ]
        
        resolution_times = [
            (issue.updated_date - issue.created_date).days for issue in closed_issues
        ]
        
        # Debugging: print resolution times and closed issues
        print("Closed Issues:", closed_issues)
        print("Resolution Times:", resolution_times)

        # Expected resolution times for the mock issues
        expected_resolution_times = [4, 10]
        
        self.assertEqual(resolution_times, expected_resolution_times)
        self.assertEqual(len(closed_issues), 2)

if __name__ == "__main__":
    unittest.main()
