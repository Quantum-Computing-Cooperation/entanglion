using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class DeleteDie : MonoBehaviour
{
    public PlayerManager playerManager;

    public void OnDelete()
    {
        NetworkIdentity networkIdentity = NetworkClient.connection.identity;
        playerManager = networkIdentity.GetComponent<PlayerManager>();
        playerManager.CmdDestroyDie();
    }

}
