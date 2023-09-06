from logging import LogRecord
import logging


class BaseFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        raise NotImplemented('filter method must be implemented')

    @staticmethod
    def _format_message(record: LogRecord) -> str:
        raise NotImplemented('_format_message method must be implemented')


class RootFilter(BaseFilter):
    def filter(self, record: logging.LogRecord):
        record.req_id = 's0m3R3q1d'
        record.message = self._format_message(record)
        return True

    @staticmethod
    def _format_message(record: logging.LogRecord) -> str:
        return record.message


class RequestsFilter(BaseFilter):
    def filter(self, record: LogRecord):
        record.req_id = 'do0m'
        record.route = 'kjfdasl'
        record.message = self._format_message(record)
        return True

    @staticmethod
    def _format_message(record: logging.LogRecord) -> str:
        return f'{record.route} {record.getMessage()}'
