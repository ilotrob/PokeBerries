from io import BytesIO
from matplotlib.pyplot import figure
import matplotlib
import matplotlib.pyplot as plt
import statistics
import base64
import requests

matplotlib.use('Agg')

class Processor:
    """
    Main class with the requiered functions to process the information
    returned from the calls to the pokemon API.
    """

    def __init__(self, URL) -> None:
        self.names = []
        self.growth_times = []
        self.growth_times_frequencies = {}
        self.URL = URL
    
    def get_names(self) -> list:
        return self.names
    
    def get_growth_times(self) -> list:
        return self.growth_times
    
    def get_min(self) -> int:
        return min(self.growth_times)
    
    def get_max(self) -> int:
        return max(self.growth_times)
    
    def get_median(self) -> int:
        return statistics.median(self.growth_times)
    
    def get_variance(self) -> int:
        return statistics.variance(self.growth_times)
    
    def get_mean(self) -> int:
        return statistics.mean(self.growth_times)

    def get_growth_times_frequencies(self) -> dict:
        self.growth_times_frequencies = {}
        for growth_time in self.growth_times:
            if growth_time not in self.growth_times_frequencies:
                self.growth_times_frequencies[growth_time] = self.growth_times.count(growth_time)

    def get_berries_info(self) -> dict:
        self.retrieve_data()
        response = {}
        response["berries_names"] = self.get_names()
        response["min_growth_time"] = self.get_min()
        response["median_growth_time"] = self.get_median()
        response["max_growth_time"] = self.get_max()
        response["variance_growth_time"] = self.get_variance()
        response["mean_growth_time"] = self.get_mean()
        response["frequency_growth_time"] = self.get_growth_times_frequencies()

        return response
    
    def retrieve_data(self) -> None:
        requests.urllib3.disable_warnings()

        try:
            payload = requests.get(self.URL,verify=False)
            data = payload.json()
            results = data["results"]
            for berry in results:
                name = berry["name"]
                berry_URL = berry["url"]
                payload = requests.get(berry_URL,verify=False)
                berry_data = payload.json()
                self.names.append(name)
                self.growth_times.append(berry_data["growth_time"])
        except Exception as e:
            print("Failed to get:")
            print(e)

    def get_histogram_html(self):
        self.retrieve_data()
        x = self.get_growth_times()

        tmpfile = BytesIO()
        bin_names = range(min(x),max(x)+1)
        figure(figsize=(12,9))
        plt.hist(x, width=0.9, bins=len(bin_names))
        plt.autoscale(enable=True)
        #plt.xticks(bin_names)
        plt.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

        #html = 'Some html head' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + 'Some more html'
        image_html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

        html = """
        <!DOCTYPE html>
        <html>
        <body>

        <title>PokeBerries Histogram</title>

        <h1>Histogram of pokeberries' growth times:</h1>
        <p>{}</p>

        </body>
        </html>
        """.format(image_html)

        return html