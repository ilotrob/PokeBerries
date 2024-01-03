from processor import Processor

URL = "https://pokeapi.co/api/v2/berry/?limit=200"

def test_get_names():
    proc = Processor(URL)

    proc.names = ["fake_berry_name"]
    assert proc.get_names()

    proc.names = ["False"]
    assert proc.get_names()

    proc.names = [False]
    assert proc.get_names()

def test_get_names_empty_list():
    proc = Processor(URL)

    assert not proc.get_names()

def test_get_growth_times():
    proc = Processor(URL)
    proc.growth_times = [0]

    assert proc.get_growth_times()

def test_get_growth_times_empty_list():
    proc = Processor(URL)

    assert not proc.get_growth_times()

def test_get_min():
    proc = Processor(URL)
    proc.growth_times = [0,1,2]

    assert proc.get_min() is not None
    assert proc.get_min() is 0

def test_get_min_empty_list():
    proc = Processor(URL)

    assert not proc.get_min()

def test_get_max():
    proc = Processor(URL)
    proc.growth_times = [0]

    assert proc.get_max() is not None
    assert proc.get_max() is 0

def test_get_max_empty_list():
    proc = Processor(URL)

    assert not proc.get_max()

def test_get_median():
    proc = Processor(URL)
    proc.growth_times = [0]

    assert proc.get_median() is not None
    assert proc.get_median() is 0

def test_get_median_empty_list():
    proc = Processor(URL)

    assert not proc.get_median()

def test_get_variance():
    proc = Processor(URL)
    proc.growth_times = [1,1,1]

    assert proc.get_variance() is not None
    assert proc.get_variance() is 0

def test_get_variance_empty_list():
    proc = Processor(URL)

    assert not proc.get_variance()

def test_get_mean():
    proc = Processor(URL)
    proc.growth_times = [0]

    assert proc.get_mean() is not None
    assert proc.get_mean() is 0

def test_get_mean_empty_list():
    proc = Processor(URL)

    assert not proc.get_mean()

def test_get_growth_times_frequencies():
    proc = Processor(URL)
    proc.growth_times = [1,1,1,0,0,2]

    frequencies = proc.get_growth_times_frequencies()
    assert frequencies[0] is 2
    assert frequencies[1] is 3
    assert frequencies[2] is 1

def test_get_growth_times_frequencies_empty_list():
    proc = Processor(URL)

    assert not proc.get_growth_times_frequencies()

def test_get_berries_info():
    proc = Processor(URL)

    response = proc.get_berries_info()

    assert len(response["berries_names"]) is proc.data["count"]
    assert len(proc.growth_times) is proc.data["count"]

    proc.names = ["Fake name"]
    proc.growth_times = [0,0,2,2,1,1,1,1,1]

    response = proc.get_berries_info()

    assert response["berries_names"][0] is "Fake name"
    assert response["min_growth_time"] is 0
    assert response["median_growth_time"] is 1
    assert response["max_growth_time"] is 2
    assert(response["variance_growth_time"] == .5)
    assert response["mean_growth_time"] is 1
    assert response["frequency_growth_time"][0] is 2
    assert response["frequency_growth_time"][1] is 5
    assert response["frequency_growth_time"][2] is 2

def test_get_berries_info_wrong_url():
    proc = Processor("DUMMY_URL")

    assert not proc.get_berries_info()

def test_retrieve_data():
    proc = Processor(URL)

    assert proc.retrieve_data()
    assert len(proc.growth_times) is proc.data["count"]
    assert len(proc.names) is proc.data["count"]

def test_retrieve_data_wrong_url():
    proc = Processor("DUMMY_URL")

    assert not proc.get_berries_info()

def test_get_histogram_html():
    proc = Processor(URL)

    html = proc.get_histogram_html()
    assert '<img src=\'data:image/png;base64,' in html

def test_get_histogram_html_wrong_url():
    proc = Processor("DUMMY_URL")

    assert not proc.get_histogram_html()