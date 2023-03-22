import React from "react";
import { Collapse, Image } from "antd";
import code_img from "../assets/code.png";

const { Panel } = Collapse;

const DropdownCollapse: React.FC = (props) => {
  return (
    <div className="px-10 py-5 lg:px-64">
      <Collapse>
        <Panel
          className="text-left"
          header="สรุป Regular expression ที่ใช้"
          key={1}
        >
          <p className="text-center">
            รูปภาพแสดงโค้ดในส่วนของการดึงข้อมูลและกรองชือวัดด้วย Regular
            expression{" / "}
            <a
              className="text-blue-600"
              target="_blank"
              href="https://github.com/poomsakk/simple_crawler_web/blob/main/back/crawler.py"
            >
              Link to this file
            </a>
            <Image
              className="p-4 flex justify-center content-center"
              src={code_img}
            />
          </p>
          <p className="leading-relaxed">
            เนื่องจากชื่อวัดที่เราต้องการนั้น อยู่ใน 'a' tag
            ดังนั้นเราจึงต้องกรอง 'a' tag ออกมาก่อน
            <br></br>- บรรทัดที่ 9 เป็นการใช้ re เพื่อกรองเอาแต่ string
            ที่ขึ้นต้นด้วย '&lt;a' และลงท้ายด้วย '&lt;/a&gt;'
            จากนั้นนำผลลัพธ์ไปเก็บไว้ใน lsit
            <br></br>- บรรทัดที่ 13 เป็นการใช้ re เพื่อกรองเอาแต่ content
            (จากเดิมเช่น &lt;a href="xxx" title="yyy"&gt;zzz&lt;/a&gt;
            เราจะเอาแค่ zzz)
            <br></br>- บรรทัดที่ 14 เก็บผลลัพธ์ไว้ใน list (จากตัวอย่างด้านบน
            group(0) คือ 'href="xxx" title="yyy"', ส่วน group(1) คือ zzz)
            <br></br>- บรรทัดที่ 19 เป็นการใช้ re เพื่อกรองหาแต่ content
            ที่ขึ้นต้นด้วยคำว่า 'วัด' เท่านั้น จากนั้นเก็บผลลัพธ์ไว้ใน list
            <br></br>- บรรทัดที่ 22 ตัดผลลัพธ์ 4 อันสุดท้ายที่เราไม่ต้องการทิ้ง
            (เป็นทุก url สำหรับ
            https://th.wikipedia.org/wiki/หมวดหมู่:รายชื่อวัดไทย)
            <br></br>ก็จะได้ผลลัพธ์สุดท้ายที่มีแต่รายชื่อวัดไทย
          </p>
        </Panel>
      </Collapse>
    </div>
  );
};

export default DropdownCollapse;
