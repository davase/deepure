/**
 * Created by KJSH-DN-0287 on 2021/7/29.
 */
const PageObj = function () {
    const self = this;
    console.log("执行了");
    self.init = () =>
    {
        self.bindevent();
    };
    self.bindevent = () =>
    {
        $("#sumbitinfo").click(function () {
            console.log("1111");
        })

        $("#exporttable").click(function () {




          console.log("开始导出数据");
          console.log("我执行了");
        })
    };
};
