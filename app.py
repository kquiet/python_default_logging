# Logging setup
from default_logging import configure_logging
configure_logging()

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Set up OpenTelemetry tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Set up logger
import logging
logger = logging.getLogger(__name__)

def main():
    with tracer.start_as_current_span("test-span"):
        logger.info("Hello with OpenTelemetry trace context!")

if __name__ == "__main__":
    main()