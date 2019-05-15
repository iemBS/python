from geopy import GoogleV3

place = "221b Baker Street, London"
location = GoogleV3().geocode(place)

print(location.address)
print(location.location)


# There’s also a useful distance class. It calculates the distance between two locations in your favorite unit of measurement.
