import edgeimpulse as ei
from datetime import datetime

ei.API_KEY = "****************************"

response = ei.experimental.data.upload_directory(
    directory="validate",
    category="testing",
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