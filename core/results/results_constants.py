# Copyright 2015 Intel Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""ResultsConstants class
"""

class ResultsConstants(object):
    """Constant fields holder used by various IResult implementations.
    """
    TYPE = 'type'
    ID = 'id'
    PACKET_SIZE = 'packet_size'
    DEPLOYMENT = 'deployment'

    UNKNOWN_VALUE = "Unknown"

    #Traffic Constants
    #RFC2544 Throughput & Continuous
    THROUGHPUT_TX_FPS = 'throughput_tx_fps'
    THROUGHPUT_RX_FPS = 'throughput_rx_fps'
    THROUGHPUT_TX_MBPS = 'throughput_tx_mbps'
    THROUGHPUT_RX_MBPS = 'throughput_rx_mbps'
    THROUGHPUT_TX_PERCENT = 'throughput_tx_percent'
    THROUGHPUT_RX_PERCENT = 'throughput_rx_percent'
    MIN_LATENCY_NS = 'min_latency_ns'
    MAX_LATENCY_NS = 'max_latency_ns'
    AVG_LATENCY_NS = 'avg_latency_ns'
    #Burst traffic
    TX_FRAMES = 'tx_frames'
    RX_FRAMES = 'rx_frames'
    TX_BYTES = 'tx_bytes'
    RX_BYTES = 'rx_bytes'
    PAYLOAD_ERR = 'payload_err'
    SEQ_ERR = 'seq_err'
    #Back2Back
    B2B_RX_FPS = 'b2b_rx_fps'
    B2B_TX_FPS = 'b2b_tx_fps'
    B2B_RX_PERCENT = 'b2b_rx_percent'
    B2B_TX_PERCENT = 'b2b_tx_percent'
    B2B_TX_COUNT = 'b2b_tx_count'
    B2B_FRAMES = 'b2b_frames'
    B2B_FRAME_LOSS_FRAMES = 'b2b_frame_loss_frames'
    B2B_FRAME_LOSS_PERCENT = 'b2b_frame_loss_percent'

    @staticmethod
    def get_traffic_constants():
        """Method returns all Constants used to store results.

        These data can be used to generate final output.

        :return: List of Strings which contains column names used as a result
        This applies to any traffic(RFC2544 throughput or continuous flow)
        operation.
        """
        return [ResultsConstants.TYPE,
                ResultsConstants.ID,
                ResultsConstants.PACKET_SIZE,
                ResultsConstants.DEPLOYMENT,
                ResultsConstants.THROUGHPUT_TX_FPS,
                ResultsConstants.THROUGHPUT_RX_FPS,
                ResultsConstants.THROUGHPUT_TX_MBPS,
                ResultsConstants.THROUGHPUT_RX_MBPS,
                ResultsConstants.THROUGHPUT_TX_PERCENT,
                ResultsConstants.THROUGHPUT_RX_PERCENT,
                ResultsConstants.MIN_LATENCY_NS,
                ResultsConstants.MAX_LATENCY_NS,
                ResultsConstants.AVG_LATENCY_NS]