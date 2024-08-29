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
    const { comments, deleteEvent } = this.props;
    const { commentText } = this.state;

    return (
      <div>
        {comments.map((comment) => (
          <div key={comment.commentid} className="d-flex align-items-center my-1">
            <p className="mb-1" style={{ margin: '0 0 0 8px', fontSize: '14px' }}>
              <a href={comment.ownerShowUrl} className="text-dark font-weight-bold mr-2">
                {comment.owner}
              </a>
              <span>{comment.text}</span>
            </p>
            {comment.lognameOwnsThis && (
              // delete button
              <button
                className="delete-comment-button ml-auto"
                onClick={() => deleteEvent(comment.commentid)}
                type="submit"
                style={{
                  margin: '0 0 0 8px',
                  background: 'none',
                  border: 'none',
                  padding: '0',
                  fontSize: '12px',
                  cursor: 'pointer',
                }}
              >
                Delete
              </button>
            )}
          </div>
        ))}
        <form onSubmit={this.handleSubmit} className="comment-form d-flex align-items-center mt-2">
          <input
            type="text"
            onChange={this.handleChange}
            value={this.state.commentText}
            placeholder="Add a comment..."
            className="form-control"
            style={{
              fontSize: '14px',
              border: 'none',
              borderBottom: '1px solid #dbdbdb',
              padding: '0 0 4px 0',
              borderRadius: '0',
              outline: 'none',
              boxShadow: 'none',
            }}
          />
          <button
            type="submit"
            className="delete-comment-button ml-auto"
            style={{
              margin: '0 0 0 8px',
              background: 'none',
              border: 'none',
              padding: '0',
              fontSize: '14px',
              cursor: 'pointer',
            }}
          >
            Post
          </button>
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
