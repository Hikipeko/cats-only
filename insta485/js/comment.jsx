import React from "react";
import PropTypes from "prop-types";

class Comment extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    // this.deleteClick = this.deleteClick.bind(this);
  }
  // deleteClick() {
  //   const { deleteEvent } = this.props;
  //   deleteEvent(this.props.comment.url);
  // }

  handleSubmit(event) {
    // console.log(`/api/v1/comments/?text=${this.state.value}&postid=3`)
    // console.log("submit handle");
    const { postid, commentEvent } = this.props;
    const { value } = this.state;
    const smturl = `/api/v1/comments/?postid=${postid}`;
    commentEvent(value, smturl);
    event.preventDefault();
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  render() {
    // console.log(this.props.comments);
    const { comments, deleteEvent } = this.props;
    return (
      <div>
        {comments.map((comment) => (
          <div key={comment.commentid}>
            <p>
              <a href={comment.ownerShowUrl}>{comment.owner}</a>
              <plaintext> {comment.text}</plaintext>
            </p>
            {comment.lognameOwnsThis && (
              <button
                className="delete-comment-button"
                onClick={() => deleteEvent(comment.commentid)}
                type="submit"
              >
                Delete
              </button>
            )}
          </div>
        ))}
        {/* <div><CommentButton postid={this.props.postid} value="" onClick={this.props.commentEvent}></CommentButton></div> */}
        <form onSubmit={this.handleSubmit} className="comment-form">
          <input type="text" onChange={this.handleChange} />
          <input type="submit" value="Comment" />
        </form>
      </div>
    );
  }
}

Comment.propTypes = {
  deleteEvent: PropTypes.func.isRequired,
  commentEvent: PropTypes.func.isRequired,
  postid: PropTypes.number.isRequired,
  comments: PropTypes.arrayOf(PropTypes.any.isRequired).isRequired,
};

export default Comment;
