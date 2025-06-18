from typing import Dict, Any

class SonarQubeError(Exception):
    """Base exception class for SonarQube related errors."""
    pass

class SonarQube:
    def __init__(self, base_url: str, session: Any) -> None:
        """Initialize SonarQube client with base URL and session."""
        self.base_url = base_url
        self.session = session

    @classmethod
    def create(cls, base_url: str, session: Any) -> 'SonarQube':
        """Create a new SonarQube instance."""
        return cls(base_url, session)

    def _get_issue_components(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue components."""
        components = {}
        if "component" in issue:
            components["component"] = issue["component"]
        if "subProject" in issue:
            components["subProject"] = issue["subProject"]
        return components

    def _get_issue_rule(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue rule information."""
        rule = {}
        if "rule" in issue:
            rule["rule"] = issue["rule"]
        return rule

    def _get_issue_severity(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue severity."""
        severity = {}
        if "severity" in issue:
            severity["severity"] = issue["severity"]
        return severity

    def _get_issue_status(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue status."""
        status = {}
        if "status" in issue:
            status["status"] = issue["status"]
        return status

    def _get_issue_message(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue message."""
        message = {}
        if "message" in issue:
            message["message"] = issue["message"]
        return message

    def _get_issue_effort(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue effort."""
        effort = {}
        if "effort" in issue:
            effort["effort"] = issue["effort"]
        return effort

    def _get_issue_debt(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue debt."""
        debt = {}
        if "debt" in issue:
            debt["debt"] = issue["debt"]
        return debt

    def _get_issue_author(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue author."""
        author = {}
        if "author" in issue:
            author["author"] = issue["author"]
        return author

    def _get_issue_tags(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue tags."""
        tags = {}
        if "tags" in issue:
            tags["tags"] = issue["tags"]
        return tags

    def _get_issue_transitions(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue transitions."""
        transitions = {}
        if "transitions" in issue:
            transitions["transitions"] = issue["transitions"]
        return transitions

    def _get_issue_actions(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue actions."""
        actions = {}
        if "actions" in issue:
            actions["actions"] = issue["actions"]
        return actions

    def _get_issue_comments(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue comments."""
        comments = {}
        if "comments" in issue:
            comments["comments"] = issue["comments"]
        return comments

    def _get_issue_assignee(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue assignee."""
        assignee = {}
        if "assignee" in issue:
            assignee["assignee"] = issue["assignee"]
        return assignee

    def _get_issue_creation_date(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue creation date."""
        creation_date = {}
        if "creationDate" in issue:
            creation_date["creationDate"] = issue["creationDate"]
        return creation_date

    def _get_issue_update_date(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue update date."""
        update_date = {}
        if "updateDate" in issue:
            update_date["updateDate"] = issue["updateDate"]
        return update_date

    def _get_issue_close_date(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue close date."""
        close_date = {}
        if "closeDate" in issue:
            close_date["closeDate"] = issue["closeDate"]
        return close_date

    def _get_issue_type(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue type."""
        type_info = {}
        if "type" in issue:
            type_info["type"] = issue["type"]
        return type_info

    def _get_issue_scope(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue scope."""
        scope = {}
        if "scope" in issue:
            scope["scope"] = issue["scope"]
        return scope

    def _get_issue_quick_fix_available(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue quick fix availability."""
        quick_fix_available = {}
        if "quickFixAvailable" in issue:
            quick_fix_available["quickFixAvailable"] = issue["quickFixAvailable"]
        return quick_fix_available

    def _get_issue_message_formattings(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue message formattings."""
        message_formattings = {}
        if "messageFormattings" in issue:
            message_formattings["messageFormattings"] = issue["messageFormattings"]
        return message_formattings

    def _get_issue_code_snippet(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and validate issue code snippet."""
        code_snippet = {}
        if "codeSnippet" in issue:
            code_snippet["codeSnippet"] = issue["codeSnippet"]
        return code_snippet

    def _extract_issue_fields(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Extract all fields from an issue."""
        fields = {}
        field_mappings = {
            "component": "component",
            "subProject": "subProject",
            "rule": "rule",
            "severity": "severity",
            "status": "status",
            "message": "message",
            "effort": "effort",
            "debt": "debt",
            "author": "author",
            "tags": "tags",
            "transitions": "transitions",
            "actions": "actions",
            "comments": "comments",
            "assignee": "assignee",
            "creationDate": "creationDate",
            "updateDate": "updateDate",
            "closeDate": "closeDate",
            "type": "type",
            "scope": "scope",
            "quickFixAvailable": "quickFixAvailable",
            "messageFormattings": "messageFormattings",
            "codeSnippet": "codeSnippet"
        }
        
        for field, key in field_mappings.items():
            if field in issue:
                fields[key] = issue[field]
                
        return fields

    def get_sonar_issues(self, project_key: str, branch: str = None) -> List[Dict[str, Any]]:
        """Get all issues for a project."""
        params = {"componentKeys": project_key}
        if branch:
            params["branch"] = branch

        response = self.session.get(f"{self.base_url}/api/issues/search", params=params)
        response.raise_for_status()

        data = response.json()
        issues = data.get("issues", [])

        return [self._extract_issue_fields(issue) for issue in issues]

    def _make_api_request(self, endpoint: str, params: Dict[str, str]) -> Dict[str, Any]:
        """Make an API request to SonarQube."""
        response = self.session.get(self.base_url + endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def _fetch_metrics_data(self, project_key: str) -> List[Dict[str, Any]]:
        """Fetch metrics data from SonarQube API."""
        data = self._make_api_request("/api/metrics/search", {"projectKeys": project_key})
        return data.get("metrics", [])

    def _extract_goutsum_value(self, metric: Dict[str, Any]) -> Dict[str, Any]:
        """Extract goutsum value from metric if available."""
        if metric.get("key") == "goutsum":
            return {"goutsum": metric.get("value")}
        else:
            # No specific handling needed for other metrics
            return {}

    def _process_metric(self, metric: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single metric and return its data."""
        return self._extract_goutsum_value(metric)

    def _aggregate_metrics(self, metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aggregate all metrics into a single dictionary."""
        return {k: v for metric in metrics for k, v in self._process_metric(metric).items()}

    def get_sonar_metrics(self, project_key: str) -> Dict[str, Any]:
        """Get all metrics for a project."""
        try:
            return self._aggregate_metrics(self._fetch_metrics_data(project_key))
        except Exception as e:
            raise SonarQubeError(f"Failed to get SonarQube metrics: {str(e)}") from e 