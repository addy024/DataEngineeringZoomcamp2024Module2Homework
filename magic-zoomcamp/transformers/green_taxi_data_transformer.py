if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero passengers: {data['trip_distance'].isin([0]).sum()}")
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    print(f"Post Processing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Post Processing: rows with zero passengers: {data['trip_distance'].isin([0]).sum()}")
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    # Rename columns using the camel_to_snake function
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )
    return data


@test
def test_zero_passenger_trip(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0

@test
def test_zero_distance_trip(output, *args) -> None:
    
    assert output['trip_distance'].isin([0]).sum() == 0

@test 
def test_vendor_id(output, *args) -> None:
    assert output['vendor_id'].isnull().sum() == 0

