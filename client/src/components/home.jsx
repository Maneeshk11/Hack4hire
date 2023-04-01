import { Link } from "react-router-dom";
// import { plusSymbol} from 
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'


const Home= () =>{

    const backgroundColorList = [
        "#8ac92638",
        "#ffb8032e",
        "#d6282839"
    ];
    const borderColorList = [
        "#8ac926",
        "#ffb703",
        "#d62828"
    ];
    return (
        <div className="mainHome">
            <div className="selectMain">
                <div>
                    <a href=""><i class="fa-regular fa-square-plus"></i></a>
                    <h2>New Task</h2>
                </div>
                <select name="courses" id="courses" className="selectCourse">
                    <option value="all">All Tasks</option>
                    <option value="upcoming">Upcoming</option> 
                    <option value="present">Present</option> 
                    <option value="Done">Finsihed</option> 
                    <option value="overdue">Overdue</option>
                </select>
            </div>
            <div className="taskHolder">
                <div className="task">
                    <div className="titleTask">
                        <h1>Title</h1>
                        <h3>created-date</h3>
                    </div>
                    <div className="contentDiv">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, et.</p>
                    </div>
                    <div className="deadlineTask">
                        <h3>type</h3>
                        <h3>deadline</h3>
                    </div>
                </div>
            </div>
        </div>
    );
  }
  export default Home;