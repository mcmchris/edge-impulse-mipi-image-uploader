import edgeimpulse as ei
from datetime import datetime

ei.API_KEY = "ei_056b076d107287ae4471a52c50e98484b07e8134d8ebbdf380adfcd56a40f27a"

response = ei.experimental.data.upload_directory(
    directory="dataset",
    category="training",
    label=None, # Will use the prefix before the '.' on each filename for the label
    metadata={
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source": "camera",
    }
)

# Check to make sure there were no failures
assert len(response.fails) == 0, "Could not upload some files"

# Save the sample IDs, as we will need these to retrieve file information and delete samples
ids = []
for sample in response.successes:
    ids.append(sample.sample_id)

# Review the sample IDs and get the associated server-side filename
# Note the lack of extension! Multiple samples on the server can have the same filename.
for id in ids:
    filename = ei.experimental.data.get_filename_by_id(id)
    print(f"Sample ID: {id}, filename: {filename}")