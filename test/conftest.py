def pytest_runtest_logreport(report):
	report.nodeid = report.nodeid.split("::", 1)[1]
