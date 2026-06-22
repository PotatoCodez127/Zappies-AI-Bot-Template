import pytest
from tools.action_schemas import CheckAvailabilityArgs

def test_pydantic_action_schemas():
    """
    Smoke Test: Verifies that the Pydantic tool argument validation schemas
    can be imported and initialized properly without requiring active 
    cloud database connections.
    """
    # Sample mock input data matching our contract schema rules
    mock_date = "2026-06-22"
    
    # Instantiate the schema structure
    schema_instance = CheckAvailabilityArgs(date=mock_date)
    
    # Assert that the data was safely assigned and parsed
    assert schema_instance.date == mock_date