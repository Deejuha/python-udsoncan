from udsoncan.BaseService import BaseService, BaseSubfunction
from udsoncan.ResponseCode import ResponseCode

__all__ = ["Authentication"]

class Authentication(BaseService):
    _sid = 0x29

    supported_negative_response = [
        ResponseCode.CertificateNotAvailable,
        ResponseCode.CertificateVerificationFailed_InvalidTimePeriod,
        ResponseCode.CertificateVerificationFailed_InvalidSignature,
        ResponseCode.CertificateVerificationFailed_InvalidChainOfTrust,
        ResponseCode.CertificateVerificationFailed_InvalidType,
        ResponseCode.CertificateVerificationFailed_InvalidFormat,
        ResponseCode.CertificateVerificationFailed_InvalidContent,
        ResponseCode.CertificateVerificationFailed_InvalidScope,
        ResponseCode.CertificateVerificationFailed_InvalidCertificate,
        ResponseCode.OwnershipVerificationFailed,
        ResponseCode.ChallengeCalculationFailed,
        ResponseCode.SettingAccessRightsFailed,
        ResponseCode.SessionKeyCreationDerivationFailed,
        ResponseCode.ConfigurationDataUsageFailed,
        ResponseCode.DeAuthenticationFailed,
    ]

    class AuthenticationTask(BaseSubfunction):
        deauthenticate = 0x00
        verify_certificate_unidirectional = 0x01
        verify_certificate_bidirectional = 0x02
        proof_of_ownership = 0x03
        transmit_certificate = 0x04
        request_challenge_for_authentication = 0x05
        verify_proof_of_ownership_unidirectional = 0x06
        verify_proof_of_ownership_bidirectional = 0x07
        authentication_configuration = 0x08
