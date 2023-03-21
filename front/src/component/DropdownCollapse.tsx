import React from "react";
import { Collapse } from "antd";

const { Panel } = Collapse;

const DropdownCollapse: React.FC = (props) => {
  return (
    <div className="px-10 pb-10">
      <Collapse className="text-left">
        <Panel header="สรุป Regular expression ที่ใช้" key={1}>
          <p>BLABLA</p>
        </Panel>
      </Collapse>
    </div>
  );
};

export default DropdownCollapse;
