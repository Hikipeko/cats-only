import React from "react";
import PropTypes from "prop-types";
import moment from "moment";
import { PostImage, UserInfo } from "./contents";
import Like from "./like";
import Comment from "./comment";

class Post extends React.Component {
  /* Display image and post owner of a single post
   */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      // comments: [],
      created: "",
      imgUrl: "",
      lognameLikesThis: false,
      numLikes: 0,
      likeUrl: null,
      owner: "",
      ownerImgUrl: "",
      ownerShowUrl: "",
      postShowUrl: "",
      postid: 0,
      comments: [],
    };
    // bind click events in constructor
    this.handleLikeClick = this.handleLikeClick.bind(this);
    this.handleUnlikeClick = this.handleUnlikeClick.bind(this);
    this.handleDeleteCommentClick = this.handleDeleteCommentClick.bind(this);
    this.handleCommentClick = this.handleCommentClick.bind(this);
  }

  componentDidMount() {
    // This line automatically assigns this.props.url to the const variable url
    const { url } = this.props;

    // Call REST API to get the post's information
    fetch(url, { credentials: "same-origin" })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          // comments: data.comments,
          created: moment(data.created).fromNow(),
          imgUrl: data.imgUrl,
          lognameLikesThis: data.likes.lognameLikesThis,
          numLikes: data.likes.numLikes,
          likeUrl: data.likes.url,
          owner: data.owner,
          ownerImgUrl: data.ownerImgUrl,
          ownerShowUrl: data.ownerShowUrl,
          postShowUrl: data.postShowUrl,
          postid: data.postid,
          comments: data.comments,
        });
      })
      .catch((error) => console.log(error));
  }

  // handler for clicking like button
  // make "POST /api/v1/likes/?postid=<postid>" request
  // and change local state without asking for whole page
  handleLikeClick() {
    const { postid, lognameLikesThis } = this.state;
    if (!lognameLikesThis) {
      const makeLikeUrl = `/api/v1/likes/?postid=${postid}`;
      console.log("POST", makeLikeUrl);
      // fetched json example:
      // {
      //     "likeid": 6,
      //     "url": "/api/v1/likes/6/"
      // }
      fetch(makeLikeUrl, {
        method: "POST",
        credentials: "same-origin",
      })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          this.setState({
            likeUrl: data.url,
          });
        })
        .catch((error) => console.log(error));
      // change local state
      const { numLikes } = this.state;
      this.setState({
        lognameLikesThis: true,
        numLikes: numLikes + 1,
      });
    } else {
      console.log("Already liked");
    }
  }

  handleCommentClick(value, url) {
    console.log("create comment");
    // const { pid } = this.state.url;
    // alert(pid);
    // const url = `/api/v1/comments/?postid=${pid}`;
    const text = { text: value };
    fetch(url, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(text),
    })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState((prevState) => ({
          comments: prevState.comments.concat([data]),
        }));
      })
      .catch((error) => console.log(error));
  }

  handleDeleteCommentClick(commentid) {
    console.log("delete comment");
    const { comments } = this.state;
    let postUrl = "/api/v1/comments/";
    postUrl += commentid;
    postUrl += "/";
    fetch(postUrl, {
      method: "DELETE",
      credentials: "same-origin",
    })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return "";
      })
      .then(() => {
        this.setState({
          comments: comments.filter((c) => c.commentid !== commentid),
        });
      })
      .catch((error) => console.log(error));
  }

  // handler for clicking unlike button
  // make "DELETE /api/v1/likes/<likeid>/" request
  // and change local state without asking for whole page
  handleUnlikeClick() {
    const { likeUrl, lognameLikesThis } = this.state;
    if (lognameLikesThis) {
      console.log("DELETE", likeUrl);
      fetch(likeUrl, {
        method: "DELETE",
        credentials: "same-origin",
      })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return "";
        })
        .then(() => {
          this.setState({
            likeUrl: null,
          });
        })
        .catch((error) => console.log(error));
      // change local state
      const { numLikes } = this.state;
      this.setState({
        lognameLikesThis: false,
        numLikes: numLikes - 1,
      });
    } else {
      console.log("Already unliked");
    }
  }

  render() {
    // This line automatically assigns this.state.imgUrl to the const variable imgUrl
    // and this.state.owner to the const variable owner
    const {
      // comments,
      created,
      imgUrl,
      lognameLikesThis,
      numLikes,
      owner,
      ownerImgUrl,
      ownerShowUrl,
      postShowUrl,
      postid,
      comments,
    } = this.state;

    // const listComments = comments.map((comment) => (
    //   <Comment
    //     key={comment.commentid}
    //     commentid={comment.commentid}
    //     text={comment.text}
    //     lognameOwnsThis={comment.lognameOwnsThis}
    //     commentEvent={this.handleCommentClick}
    //     deleteEvent={this.handleDeleteCommentClick}
    //     commentUrl={comment.url}
    //     owner={comment.owner}
    //   />))

    // Render post image and post owner
    return (
      <div className="post my-2">
        <div className="card">
          <UserInfo
            ownerImgUrl={ownerImgUrl}
            ownerShowUrl={ownerShowUrl}
            owner={owner}
            created={created}
            postid={postid}
            postShowUrl={postShowUrl}
          />
          <PostImage imgUrl={imgUrl} likeEvent={this.handleLikeClick} />
          <Like
            postid={postid} // only for debug print
            lognameLikesThis={lognameLikesThis}
            numLikes={numLikes}
            likeEvent={this.handleLikeClick}
            unlikeEvent={this.handleUnlikeClick}
          />
          <Comment
            commentEvent={this.handleCommentClick}
            deleteEvent={this.handleDeleteCommentClick}
            comments={comments}
            postid={postid}
          />
        </div>
      </div>
    );
  }
}

Post.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Post;
