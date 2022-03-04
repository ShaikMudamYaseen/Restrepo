import random as rnd
import prettytable


class Data:
    ROOMS = [["R1", 25], ["R2", 45], ["R3", 35]]
    MEETING_TIMES = [['MT1', "MWF 09:00 - 10:00"],
                     ['MT2', "MWF 09:00 - 10:00"],
                     ['MT3', "TTH 09:00 - 10:00"]
                     ['MT4', "TTH 09:00 - 10:00"]]
    INSTRUCTIONS = [["I1", "ramesh"],
                    ["I2", "prashanth"],
                    ["I3", "pavan"],
                    ["I4", "sreesha"]]

    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(
                self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(0, len(self.INSTRUCTIONS)):
            self._instructors.append(Instructor(
                self.INSTRUCTIONS[i][0], self.INSTRUCTIONS[i][1]))
        Course1 = Course(
            "c1", "325k", [self._instructors[0], self._instructors[1]], 25)
        Course2 = Course(
            "c2", "319k", [self._instructors[0], self._instructors[1]], 35)
        Course3 = Course(
            "c3", "462k", [self._instructors[0], self._instructors[1]], 25)
        Course4 = Course(
            "c4", "464k", [self._instructors[0], self._instructors[1]], 30)


class Schedule:
    def __int__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimes()[
                                         rnd.randrange(0, len(data.get_rooms()))])
                newClass.set_instructor(courses[j].get_instructor(
                )[rnd.randrange(0, len(courses[j].get_instructors()))])
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents()):
                self._numbOfConflicts += 1
            for j in range(0, len(classes)):
                if (j >= 1):
                    if (classes[i].get_meetingCapacity() < classes[i].get_meetingTime() and classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room() == classes[j].get_room()):
                            self._numbOfConflicts += 1
                        if (classes[i].get_instructor() == classes[j].get_instructor()):
                            self._numbOfConflicts += 1
        return 1/((1.0*self._numbOfConflicts+1))


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())

    def get_schedules(self): return self._schedules


class Genetic:
    ''' '''


class Course:
    def __init__(self, number, name, instructors, maxNumberofStudents):
        self._number = number
        self._name = name
        self._maxNumberofStudent = maxNumberofStudents
        self._instructors = instructors

    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_instructors(self): return self._instructors
    def __str__(self): return self._name


class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name


class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity

    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity


class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def get_id(self): return self._id
    def get_time(self): return self._time


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self): return self._name
    def get_courses(self): return self._courses


class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meatingTime = None
        self._room = None

    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meatingTime
    def get_room(self): return self._room
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meatingTime): self._meatingTime = meatingTime
    def set_room(self, room): self._room = room

    def __str__(self):
        return str(self._dept.get_name()+","+str(self._course.get_number())+"," +
                   str(self._room.get_number())+","+str(self._instructor.get_id())+","+str(self._meatingTime.get_id()))


class DisplayMgr:
    def print_available_data(self):
        print("alll available data")
        self.print_data()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_time()

    def print_dept():
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_course()
            tempStr = "["
            for j in range(0, len(courses)-1):
                tempStr += courses[j].__ste__()+","
                tempStr += courses[len(courses)-1].__str__() + "]"
                availableDeptsTable.add_row(
                    [depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)


data = Data()
