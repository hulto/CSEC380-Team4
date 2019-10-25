'use strict';

const e = React.createElement;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    <h1>Hello World</h1>
    // if (this.state.liked) {
    //   return 'You liked comment number ' + this.props.commentID;
    // }

    // return e(
    //   'button',
    //   { onClick: () => this.setState({ liked: true }) },
    //   'Like'
    // );
  }
}

//ReactDOM.render(<App />, document.getElementById("root"));
// Find all DOM containers, and render Like buttons into them.
document.querySelectorAll('.root')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    // const commentID = parseInt(domContainer.dataset.commentid, 10);
    ReactDOM.render(
      e(App, { commentID: commentID }),
      domContainer
    );
  });
