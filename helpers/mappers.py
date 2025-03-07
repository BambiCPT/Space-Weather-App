
class PlanetaryKIndex:
    def __init__(self, kp, estimated_kp, time):
        self.kp: str = kp
        self.estimated_kp: str = estimated_kp
        self.time: str = time


class XRayFlare:
    def __init__(self, begin_time, max_class_time, max_class, end_time):
        self.begin_time: str = begin_time
        self.end_time: str = end_time
        self.max_class_time: str = max_class_time
        self.max_class: str = max_class


class SolarProbability:
    def __init__(self, class_c_1_day, class_c_2_day, class_c_3_day, class_m_1_day, class_m_2_day, class_m_3_day, class_x_1_day, class_x_2_day, class_x_3_day, time):
        self.class_c_1_day: str = class_c_1_day
        self.class_c_2_day: str = class_c_2_day
        self.class_c_3_day: str = class_c_3_day
        self.class_m_1_day: str = class_m_1_day
        self.class_m_2_day: str = class_m_2_day
        self.class_m_3_day: str = class_m_3_day
        self.class_x_1_day: str = class_x_1_day
        self.class_x_2_day: str = class_x_2_day
        self.class_x_3_day: str = class_x_3_day
        self.time: str = time


class Mappers:
    def planetary_kp(self, data):
        mapped_kp = []

        for item in data:
            planetaryKpi = PlanetaryKIndex(
                kp=item["kp"],
                estimated_kp=item["estimated_kp"],
                time=item["time_tag"],
            )
            mapped_kp.append(planetaryKpi)

        return mapped_kp

    def xray_flare(self, data):
        mapped_flares = []

        for item in data:
            # Remove the Z from the timestampt as it ment to indicate Zulu time also known as UTC
            flare_obj = XRayFlare(
                begin_time=item["begin_time"].replace("Z", ''),
                end_time=item["end_time"].replace("Z", ''),
                max_class_time=item["max_time"].replace("Z", ''),
                max_class=item["max_class"],
            )
            mapped_flares.append(flare_obj)

        return mapped_flares

    def solar_proability(self, data):
        mapped_probability = []

        for item in data:
            probability_obj = SolarProbability(
                class_c_1_day=item["c_class_1_day"],
                class_c_2_day=item["c_class_2_day"],
                class_c_3_day=item["c_class_3_day"],
                class_m_1_day=item["m_class_1_day"],
                class_m_2_day=item["m_class_2_day"],
                class_m_3_day=item["m_class_3_day"],
                class_x_1_day=item["x_class_1_day"],
                class_x_2_day=item["x_class_2_day"],
                class_x_3_day=item["x_class_3_day"],
                time=item["date"]
            )
            mapped_probability.append(probability_obj)

        return mapped_probability
