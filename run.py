

"""
Starting point of the application. This module is invoked from
the command line to run the analyses.
"""

import argparse

import config
from example_analysis import ExampleAnalysis

from usage_analysis import  UsageAnalysis
from TriageAnalysis import IssueTriageAnalyser 
from CommonIssueAnalyser import CommonIssuesAnalyser
from tree_visualizer import IssueTreeVisualizer


def parse_args():
    """
    Parses the command line arguments that were provided along
    with the python command. The --feature flag must be provided as
    that determines what analysis to run. Optionally, you can pass in
    a user and/or a label to run analysis focusing on specific issues.
    
    You can also add more command line arguments following the pattern
    below.
    """
    ap = argparse.ArgumentParser("run.py")
    
    # Required parameter specifying what analysis to run
    ap.add_argument('--feature', '-f', type=int, required=True,
                    help='Which of the three features to run')
    
    # Optional parameter for analyses focusing on a specific user (i.e., contributor)
    ap.add_argument('--user', '-u', type=str, required=False,
                    help='Optional parameter for analyses focusing on a specific user')
    
    # Optional parameter for analyses focusing on a specific label
    ap.add_argument('--label', '-l', type=str, required=False,
                    help='Optional parameter for analyses focusing on a specific label')
    ap.add_argument(
        'file_path', 
        type=str, default='data/poetry_issues.json', 
        help='Path to the JSON file containing issues.'
        )
    ap.add_argument('--issue_limit', type=int, default=100, help='Limit the number of issues to process.')
    ap.add_argument('--start_date', type=str, help='Start date in ISO format (YYYY-MM-DD).')
    ap.add_argument('--end_date', type=str, help='End date in ISO format (YYYY-MM-DD).')
    
    return ap.parse_args()



# Parse feature to call from command line arguments
args = parse_args()
# Add arguments to config so that they can be accessed in other parts of the application
config.overwrite_from_args(args)
    
# Run the feature specified in the --feature flag
if args.feature == 0:
    ExampleAnalysis().run()
elif args.feature == 1:
    UsageAnalysis().run()
elif args.feature == 2:
    pass # TODO call second analysis
# function with parameter
elif args.feature == 3:
    IssueTreeVisualizer('data/poetry_issues.json').run()
else:
    print('Need to specify which feature to run with --feature flag.')
