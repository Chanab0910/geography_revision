import random

class Work:
    def __init__(self):
        self.topics = ['SEZ','Rana' 'Plaza','World Bank','IMF','WTO','SWFs','Trade blocs','Coffee','apple',
                       'belt and road','Antarctica threats','Antarctica mitigation','Qatar','Banglatown - Endogenous',
                       'Banglatown - Exogenous', 'Banglatown - social inequality', 'Banglatown - Demographic change',
                       'Banglatown - economic change', 'Banglatown - North vs South','Highgate - Endogenous',
                       'Highgate - Exogenous', 'Highgate - social inequality', 'Highgate - Demographic change',
                       'Highgate - economic change','Wales','Scotland','Port Talbot','great Portland road',
                       'Alaska and transatlantic pipeline'
                       'Russian gas','fracking',
                       'OPEC / choke points / pirates',
                       'GERD',
                       'Steel dumping',
                       'Singapore',
                       'LIC water strategies',
                       '3 gorges dam',
                       'Coca Cola and india',
                       'SW USA',
                       'BP',
                       'Tar sands',
                       'Kenecott Bingham mine']
        self.globalisation = ['SEZ','Rana Plaza','World Bank','IMF','WTO','SWFs','Trade blocs','Coffee','apple',
                       'belt and road','Antarctica threats','Antarctica mitigation','Qatar']
        self.changing_places = ['Banglatown - Endogenous',
                       'Banglatown - Exogenous', 'Banglatown - social inequality', 'Banglatown - Demographic change',
                       'Banglatown - economic change', 'Banglatown - North vs South','Highgate - Endogenous',
                       'Highgate - Exogenous', 'Highgate - social inequality', 'Highgate - Demographic change',
                       'Highgate - economic change','Wales','Scotland','Port Talbot','great Portland road',]
        self.resources = ['Alaska and transatlantic pipeline',
                       'Russian gas','fracking',
                       'OPEC / choke points / pirates',
                       'GERD',
                       'Steel dumping',
                       'Singapore',
                       'LIC water strategies',
                       '3 gorges dam',
                       'Coca Cola and india',
                       'SW USA',
                       'BP',
                       'Tar sands',
                       'Kenecott Bingham mine']

        self.wrong = []
        self.right = []

    def controller(self):
        self.choose_option()
        self.other_rounds()

    def choose_option(self):
        topic = input('Do you want to test all of the topics or just one (all/one): ')
        if topic.lower() == 'all':
            self.initial_phase(self.topics)
        else:
            try:
                spec = int(input('Do you want to learn (1)Globalisation, (2)Changing Places, or (3)Resource Management: '))
                if spec == 1:
                    self.initial_phase(self.globalisation)
                elif spec == 2:
                    self.initial_phase(self.changing_places)
                elif spec == 3:
                    self.initial_phase(self.resources)
                else:
                    print("I dont know how you've managed to not select an appropriate answer, but it looks like you are "
                          "going to have to restart the program")
            except:
                print("I dont know how you've managed to not select an appropriate answer, but it looks like you are "
                      "going to have to restart the program")


    def initial_phase(self, list):
        for i in range(len(list)):
            a = random.randint(0,len(list)-1)
            print('__________________________________________________')
            print('\n')
            print(list[a])
            print('\n')
            answer = input('Did you know it?(y/n): ')
            if answer == 'y':
                self.right.append(list[a])
            else:
                self.wrong.append(list[a])
            list.pop(a)
        print('__________________________________________________')
        print('\n')
        print('You have finished going through all the terms for the first time')
        print('\n')
        self.other_rounds()

    def other_rounds(self):
        stop = False
        while not stop:
            a = random.randint(1,100)
            if a <=70 and len(self.wrong)!=0:
                r = random.randint(0,len(self.wrong)-1)
                print('__________________________________________________')
                print('\n')
                print(self.wrong[r])
                print('\n')
            else:
                r = random.randint(0, len(self.right)-1)
                print('__________________________________________________')
                print('\n')
                print(self.right[r])
                print('\n')

            answer = input('Did you know it?(y/n): ')
            if answer == 'y':
                self.right.append(list[a])
                if a <= 70:
                    self.wrong.pop(r)
                else:
                    self.right.pop(r)
            else:
                self.wrong.append(list[a])
                if a > 70:
                    self.right.pop(r)
                else:
                    self.wrong.pop(r)





if __name__ == '__main__':
    w = Work()
    print(w.choose_option())