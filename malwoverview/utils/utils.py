from urllib.parse import urlparse
import geocoder
import socket

def urltoip(url_target):
    """
    Resolves a URL to its IP address and attempts to geolocate it.

    Args:
        url_target (str): The URL to resolve.

    Returns:
        str: The city of the geolocated IP address, or "Not Found" if the IP address cannot be resolved or geolocated.
    """
    try:
        # Parse the URL to extract the network location
        target = urlparse(url_target)
        result = target.netloc

        # Resolve the network location to an IP address
        final_ip = socket.gethostbyname(result)

        # Attempt to geolocate the IP address
        geoloc = geocoder.ip(final_ip)

        # Return the city of the geolocated IP address, or "Not Found" if it cannot be geolocated
        return geoloc.city if geoloc else "Not Found"
    except Exception as e:
        # Log the exception and return "Not Found"
        print(f"An error occurred: {e}")
        return "Not Found"
