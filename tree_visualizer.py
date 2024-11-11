import json
import networkx as nx
import matplotlib.pyplot as plt
import logging

class IssueTreeVisualizer:
    def __init__(self, file_path: str, issue_limit: int = 100):
        self.file_path = file_path
        self.issue_limit = issue_limit
        self.relevant_event_types = ['labeled', 'commented', 'cross-referenced', 'closed', 'opened']
        logging.basicConfig(level=logging.INFO)

    def load_issues(self):
        logging.info("Loading issues from JSON file...")
        with open(self.file_path, 'r') as file:
            issues = json.load(file)
        logging.info(f"Loaded {len(issues)} issues.")
        return issues

    def build_graph(self, issues):
        logging.info("Building graph...")
        G = nx.DiGraph()

        for i, issue in enumerate(issues):
            if i >= self.issue_limit:
                break

            issue_number = issue.get('number')
            issue_title = issue.get('title', 'No Title')
            issue_state = issue.get('state', 'open')
            issue_color = 'green' if issue_state == 'open' else 'red'

            G.add_node(issue_number, label=issue_title, color=issue_color)

            for event in issue.get('events', []):
                event_type = event.get('event_type')
                if event_type not in self.relevant_event_types:
                    continue

                event_author = event.get('author', 'unknown')
                event_date = event.get('event_date', 'unknown')
                event_label = event.get('label', '')

                event_node = f"{issue_number}_{event_type}_{event_date}"
                G.add_node(event_node, label=f"{event_type} by {event_author} on {event_date}", color='blue')
                G.add_edge(issue_number, event_node)

                if event_type == 'cross-referenced':
                    referenced_issue = event.get('comment', '').split('#')[-1]
                    if referenced_issue.isdigit():
                        G.add_edge(event_node, int(referenced_issue))

        logging.info("Graph built successfully.")
        return G

    def draw_graph(self, G):
        logging.info("Drawing graph...")
        pos = nx.spring_layout(G)
        colors = [G.nodes[node]['color'] for node in G.nodes]
        labels = {node: G.nodes[node]['label'] for node in G.nodes}

        plt.figure(figsize=(15, 15))
        nx.draw(G, pos, node_color=colors, with_labels=True, labels=labels, font_size=8, node_size=500, font_color='black')
        plt.show()
        logging.info("Graph drawn successfully.")

    def run(self):
        issues = self.load_issues()
        G = self.build_graph(issues)
        self.draw_graph(G)