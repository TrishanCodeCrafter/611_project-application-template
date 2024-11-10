import matplotlib.pyplot as plt
import pandas as pd

class Issue:
    def __init__(self, created_date, updated_date, state):
        self.created_date = created_date
        self.updated_date = updated_date
        self.state = state

class IssueTracker:
    def __init__(self, issues):
        self.issues = issues
    
    def resolution_time_analysis(self):
        """
        Analyze and plot the resolution times of issues from open to close.
        """
        # Filter out issues that are still open (no resolution time)
        closed_issues = [issue for issue in self.issues if issue.state == 'closed']
        
        # Calculate resolution times
        resolution_times = [
            (pd.to_datetime(issue.updated_date) - pd.to_datetime(issue.created_date)).days
            for issue in closed_issues
        ]
        
        # Plot histogram of resolution times
        plt.figure(figsize=(14, 8))
        plt.hist(resolution_times, bins=20, edgecolor='black')
        plt.title("Resolution Times for Issues (in Days)")
        plt.xlabel("Days to Resolve")
        plt.ylabel("Number of Issues")
        plt.show()

# Example usage
issues = [
    Issue("2024-01-01", "2024-01-10", "closed"),
    Issue("2024-02-01", "2024-02-20", "closed"),
    Issue("2024-03-01", "2024-03-15", "open"),  # This issue is still open
]

tracker = IssueTracker(issues)
tracker.resolution_time_analysis()
