from dataclasses import dataclass


@dataclass
class Report:
	test_name: str
	nodeid: str
	error_msg: str
	status: str
