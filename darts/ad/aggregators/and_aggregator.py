"""
And Aggregator
--------------

Aggregator that identifies a time point as anomalous only if it is
included in all the input anomaly lists.
"""

from typing import Sequence

from darts import TimeSeries
from darts.ad.aggregators.aggregators import NonFittableAggregator


class AndAggregator(NonFittableAggregator):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self):
        return "AndAggregator"

    def _predict_core(self, list_series: Sequence[TimeSeries]) -> Sequence[TimeSeries]:

        return [
            series.sum(axis=1).map(lambda x: (x >= series.width).astype(float))
            for series in list_series
        ]