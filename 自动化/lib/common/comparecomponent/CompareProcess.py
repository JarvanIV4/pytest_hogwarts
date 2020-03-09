class CompareProess:

    def compare_dict_n(self, real_dict, expected_dict, des_dict= None, pre_dict=None):
        """
        比对并返回相关信息
        :param real_dict: 实际值
        :param expected_dict: 预期值
        :param des_dict: key值描述信息
        :param pre_dict: 实际值原有记录 比对结果、比对成功字段结果列表、比对失败字段结果列表、未比对字段结果列表

        """
        self.__log_list = []
        self.__errlog_list = []
        self.__surcesslog_list = []
        self.__log_add_list = []
        des_dict = des_dict or {}
        pre_dict = pre_dict or {}
        compile_dict_flag = True
        self.__is_print_pre_info = bool(pre_dict)
        self.__is_real_dict = True
        self.__is_exp_dict = True

        if expected_dict is None and real_dict is None:
            raise Exception("实际值与预期值都为None")

        if real_dict is None:
            real_dict = {}
            compile_dict_flag = False
            self.__is_real_dict = False

        if expected_dict is None:
            expected_dict = {}
            compile_dict_flag = False
            self.__is_exp_dict = False

        for key, value in expected_dict.items():
            if key in real_dict:
                try:
                    result, real_val_str, exp_val_str = self.compare_value(real_dict[key], value)
                except Exception as e:
                    raise Exception("比对字段{}时出错--{}".format(key, e.message))
            else:
                result, real_val_str, exp_val_str = False, "对应key值不存在", \
                                                    value.pattern if isinstance(value, self.__re_type) else value
            # 更新最终比对结果
            if compile_dict_flag:
                compile_dict_flag = result
            # 记录比对内容
            self.__log_list.append((key, result, pre_dict.get(key), real_val_str, exp_val_str, des_dict.get(key, "")))
            # 记录比对失败与比对成功的字段信息
            if not result:
                self.__errlog_list.append((key, result, pre_dict.get(key), real_val_str, exp_val_str, des_dict.get(key, "")))
            else:
                self.__surcesslog_list.append((key, result, pre_dict.get(key), real_val_str, exp_val_str, des_dict.get(key, "")))
        # 不参与比对的信息
        for key, val in real_dict.items():
            if key not in expected_dict:
                self.__log_add_list.append((key, None, pre_dict.get(key, ""), val, "", des_dict.get(key, "")))
        # 返回参与比对信息列表，比对失败信息列表， 未比较字段信息列表
        return compile_dict_flag, self.__log_list, self.__errlog_list, self.__surcesslog_list, self.__log_add_list


