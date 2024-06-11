import React from 'react';

const Message = ({ message }) => {
    const myStyle = "message " + message.style
    const hiddenTag = message.content ? false : true

    return (
        <div className={myStyle} hidden={hiddenTag}>
            <p><b>{message.author}:</b></p>
            <p>{message.content}</p>
        </div>
    );
};

export default Message;
