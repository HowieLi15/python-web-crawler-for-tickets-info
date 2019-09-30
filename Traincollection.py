from prettytable import PrettyTable


class Traincollection:
    header='车次 车站 时间 历时 一等 二等 高级软卧 软卧 硬卧 硬座 无座'.split()
    def __init__(self, available_train, available_place, options):
        self.available_train=available_train;
        self.available_place=available_place;
        self.options=options;
    @property
    def train(self):
        for raw_train in self.available_train:
            raw_train_list=raw_train.split('|')
            train_no=raw_train_list[3]
            initial=train_no[0].lower()
            duration=raw_train_list[10]
            if not self.options or initial in self.options:
                train = [
                    train_no,  # train number
                    '\n'.join([self.available_place[raw_train_list[6]],  #
                               self.available_place[raw_train_list[7]]]),  #
                    '\n'.join([raw_train_list[8],  #
                               raw_train_list[9]]),  #
                    duration,  #
                    raw_train_list[-6] if raw_train_list[-6] else '--',  #
                    raw_train_list[-7] if raw_train_list[-7] else '--',  #
                    raw_train_list[-15] if raw_train_list[-15] else '--',  #
                    raw_train_list[-8] if raw_train_list[-8] else '--',  #
                    raw_train_list[-14] if raw_train_list[-14] else '--',  #
                    raw_train_list[-11] if raw_train_list[-11] else '--',  #
                    raw_train_list[-9] if raw_train_list[-9] else '--',  #
                ]
                yield train

    def pretty_table(self):
        pt=PrettyTable()
        pt._set_field_names(self.header)
        for train_s in self.train:
            pt.add_row(train_s)
        print(pt)




