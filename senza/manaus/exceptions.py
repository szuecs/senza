class ManausException(Exception):
    """
    Base class for Manaus exceptions
    """


class InvalidState(ManausException):
    """
    Exception raised when executing an action would try to change a stack
    to an invalid state
    """


class ELBNotFound(ManausException):
    """
    Error raised when the ELB is not found
    """

    def __init__(self, domain_name: str):
        super().__init__('ELB not found: {}'.format(domain_name))


class HostedZoneNotFound(ManausException):
    """
    Error raised when the Route53 hosted zone is not found
    """

    def __init__(self, name: str):
        super().__init__('Hosted Zone not found: {}'.format(name))


class RecordNotFound(ManausException):
    """
    Error raised when the Route53 record is not found
    """

    def __init__(self, name: str):
        super().__init__('Route 53 Record not found: {}'.format(name))


class VPCError(ManausException, AttributeError):
    """
    Error raised when there are issues with VPCs configuration
    """

    def __init__(self, message: str, number_of_vpcs: int=None):
        super().__init__(message)
        self.number_of_vpcs = number_of_vpcs
