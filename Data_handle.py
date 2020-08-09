class DataHandle():
    # 薪资处理
    def DealSalary(self,Salary):

        Salary = Salary.replace("-","")

        Salary_min = Salary.split("k")[0]
        Salary_max = Salary.split("k")[1]

        return Salary_min,Salary_max

    # 公司规模处理
    def DealCompanySize(self,Company_size):
        if Company_size == "2000人以上":
            Company_size = Company_size.replace("2000人以上","2000-2000")
        elif Company_size == "少于15人":
            Company_size = Company_size.replace("少于15人","0-15")
        else:
            Company_size = Company_size.replace("人","")

        Company_size_Min = Company_size.split("-")[0]
        Company_size_Max = Company_size.split("-")[1]

        return Company_size_Min,Company_size_Max

    # 工作年限要求处理
    def DealWorkingSeniorityRequirements(self,Working_Seniority_Requirements):
        if Working_Seniority_Requirements == "不限":
            Working_Seniority_Requirements = Working_Seniority_Requirements.replace("不限","0-10")
        elif Working_Seniority_Requirements == "1年以下":
            Working_Seniority_Requirements = Working_Seniority_Requirements.replace("1年以下","0-1")
        elif Working_Seniority_Requirements == "应届毕业生":
            Working_Seniority_Requirements = Working_Seniority_Requirements.replace("应届毕业生","0-0")
        elif Working_Seniority_Requirements == "10年以上":
            Working_Seniority_Requirements = Working_Seniority_Requirements.replace("10年以上", "10-10")
        else:
            Working_Seniority_Requirements = Working_Seniority_Requirements.replace("年","")

        Working_Seniority_Requirements_Min = Working_Seniority_Requirements.split("-")[0]
        Working_Seniority_Requirements_Max = Working_Seniority_Requirements.split("-")[1]

        return Working_Seniority_Requirements_Min,Working_Seniority_Requirements_Max

    # 处理空的 城区 值
    def DealAreaNull(self,Area):
        if Area == "":
            Area = "其他"
        return Area

    # 处理空的 行业 值
    def DealIndustryNull(self,Industry):
        if Industry == "":
            Industry = "其他"
        return Industry

    # 处理发布日期
    def DealPublishData(self,Publish_Data):
        Publish_Data = Publish_Data.split(" ")[0]
        return Publish_Data

if __name__ == '__main__':
    DataHandle = DataHandle()