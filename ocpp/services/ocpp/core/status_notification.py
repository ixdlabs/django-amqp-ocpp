from ocpp.services.ocpp.base import OCPPMiddleware, OCPPRequest, OCPPResponse
from ocpp.types.charge_point_status import ChargePointStatus
from ocpp.types.charge_point_error import ChargePointError


class StatusNotificationMiddleware(OCPPMiddleware):
    def handle(self, req: OCPPRequest) -> OCPPResponse:
        message = req.message
        charge_point = message.charge_point

        if message.data["connectorId"] > 0:
            raise NotImplementedError(
                "The central server does not support status notifications for individual connectors"
            )
        charge_point.error_code = ChargePointError(message.data["errorCode"])
        charge_point.status = ChargePointStatus(message.data["status"])

        charge_point.vendor_error_code = message.data.get("vendorErrorCode") or ""
        charge_point.vendor_status_info = message.data.get("info") or ""
        charge_point.vendor_status_id = message.data.get("vendorId") or ""
        charge_point.save(
            update_fields=[
                "status",
                "vendor_error_code",
                "vendor_status_info",
                "vendor_status_id",
            ]
        )
        return self.next.handle(req)
