
class PlanetaryKIndex:
    def __init__(self, kp, estimated_kp, time):
        self.kp = kp
        self.estimated_kp = estimated_kp
        self.time = time

    # def __repr__(self):
    #     return f"PlanetaryKIndex(time_tag={self.time_tag}, kp_index={self.kp_index}, estimated_kp={self.estimated_kp}, kp={self.kp}\n)"

    def kpi_index_mapper(self, string):
        mapped_pki = []

        for item in string:
            pki_obj = PlanetaryKIndex(
                kp=item["kp"],
                estimated_kp=item["estimated_kp"],
                time=item["time_tag"],
            )
            mapped_pki.append(pki_obj)

        return mapped_pki


class XRayFlare:
    def __init__(self, begin_time, max_class_time, max_class, end_time):
        self.begin_time = begin_time
        self.end_time = end_time
        self.max_class_time = max_class_time
        self.max_class = max_class

#    def __repr__(self):
#         return f"XRayFlare(begin_time={self.begin_time}, end_time={self.end_time}, max_time={self.max_class_time}, max_class={self.max_class}\n)"

    def xray_flare_mapper(self, string):
        mapped_flares = []

        for item in string:
            flare_obj = XRayFlare(
                begin_time=item["begin_time"],
                end_time=item["end_time"],
                max_class_time=item["max_time"],
                max_class=item["max_class"],
            )
            mapped_flares.append(flare_obj)

        return mapped_flares


class SolarProbability:
    def __init__(self, class_c_1_day, class_c_2_day, class_c_3_day, class_m_1_day, class_m_2_day, class_m_3_day, class_x_1_day, class_x_2_day, class_x_3_day, time):
        self.class_c_1_day = class_c_1_day
        self.class_c_2_day = class_c_2_day
        self.class_c_3_day = class_c_3_day
        self.class_m_1_day = class_m_1_day
        self.class_m_2_day = class_m_2_day
        self.class_m_3_day = class_m_3_day
        self.class_x_1_day = class_x_1_day
        self.class_x_2_day = class_x_2_day
        self.class_x_3_day = class_x_3_day
        self.time = time

    def solar_proability_mapper(self, string):
        mapped_probability = []

        for item in string:
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
