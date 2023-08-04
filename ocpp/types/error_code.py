from ocpp.utils.model.model_enum import ModelEnum


class ErrorCode(ModelEnum):
    NotImplemented = "NotImplemented"
    NotSupported = "NotSupported"
    InternalError = "InternalError"
    ProtocolError = "ProtocolError"
    SecurityError = "SecurityError"
    FormationViolation = "FormationViolation"
    PropertyConstraintViolation = "PropertyConstraintViolation"
    OccurenceConstraintViolation = "OccurenceConstraintViolation"
    TypeConstraintViolation = "TypeConstraintViolation"
    GenericError = "GenericError"

    @staticmethod
    def from_exception(exception):
        if isinstance(exception, NotImplementedError):
            return ErrorCode.NotImplemented
        # elif isinstance(exception, NotSupportedError):
        #     return ErrorCode.NotSupported
        # elif isinstance(exception, InternalError):
        #     return ErrorCode.InternalError
        # elif isinstance(exception, ProtocolError):
        #     return ErrorCode.ProtocolError
        # elif isinstance(exception, SecurityError):
        #     return ErrorCode.SecurityError
        elif isinstance(exception, ValueError):
            return ErrorCode.FormationViolation
        # elif isinstance(exception, PropertyConstraintViolationError):
        #     return ErrorCode.PropertyConstraintViolation
        # elif isinstance(exception, OccurenceConstraintViolationError):
        #     return ErrorCode.OccurenceConstraintViolation
        # elif isinstance(exception, TypeConstraintViolationError):
        #     return ErrorCode.TypeConstraintViolation
        else:
            # return ErrorCode.GenericError
            return ErrorCode.InternalError
